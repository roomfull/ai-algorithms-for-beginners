"""Task 4: 案例和独立数学验证，先写测试再实现。"""
from pathlib import Path
import subprocess
import json
import math
import sys
import re
from fractions import Fraction
from decimal import Decimal, localcontext
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MLNeuralTests(unittest.TestCase):
    def run_solution(self, pid, raw, line_modes=None):
        path = ROOT/'solutions'/f'P{pid:03}.py'
        self.assertTrue(path.is_file(), f'缺少参考实现 P{pid:03}')
        result = subprocess.run([sys.executable, str(path)], input=raw,
                                text=True, capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr)
        actual=result.stdout.splitlines()
        if line_modes:
            self.assertEqual(len(actual),len(line_modes))
            for line,mode in zip(actual,line_modes):
                if mode == 'int':
                    self.assertTrue(all(re.fullmatch(r'[+-]?[0-9]+',v) for v in line.split()),line)
        return [[float(v) for v in line.split()] for line in actual]

    def test_all_independently_derived_cases(self):
        for pid in range(39,59):
            folder = '05_machine_learning' if pid<=50 else '06_neural_networks'
            path = ROOT/'chapters'/folder/'problems'/f'P{pid:03}'/'cases.json'
            if not path.is_file():
                continue  # 分批TDD；最后由题数测试保证全20题。
            data = json.loads(path.read_text(encoding='utf-8'))
            self.assertGreaterEqual(len(data['cases']),5)
            for c in data['cases']:
                with self.subTest(pid=pid,case=c['name']):
                    modes=c.get('line_modes') or [data['mode']]*len(c['expected'].splitlines())
                    actual=self.run_solution(pid,c['input'],modes)
                    wanted=[[float(v) for v in line.split()] for line in c['expected'].splitlines()]
                    self.assertEqual([len(r) for r in actual],[len(r) for r in wanted])
                    for a,b in zip(actual,wanted):
                        for x,y in zip(a,b):
                            self.assertTrue(math.isclose(x,y,abs_tol=1e-6,rel_tol=1e-6),(x,y))

    def test_knn_distance_and_vote_ties_are_distinct(self):
        self.assertEqual(self.run_solution(40,'2 1 1\n8 1\n2 -1\n0\n'),[[8]])
        self.assertEqual(self.run_solution(40,'2 1 2\n8 1\n2 -1\n0\n'),[[2]])

    def test_sigmoid_classification_uses_exact_decimal_score_sign(self):
        # Fraction从原字符串构造，独立核对9.1+0.2-9.3精确为0。
        exact=sum(Fraction(t) for t in ('9.1','0.2','-9.3'))
        self.assertEqual(exact,0)
        self.assertEqual(self.run_solution(45,'1 3\n1 1 1\n9.1 0.2 -9.3\n0\n', ['float','int']),[[0.5],[1]])
        # 输出概率会显示0.5，但精确负分数的标签仍必须为0。
        self.assertEqual(self.run_solution(45,'1 1\n-0.000001\n0.000001\n0\n', ['float','int']),[[0.5],[0]])

    def test_cart_decimal_midpoint_goes_left_without_boundary_epsilon(self):
        midpoint=(Fraction('-0.4')+Fraction('-0.2'))/2
        self.assertEqual(midpoint,Fraction('-0.3'))
        raw='2 1 4 1\n0 -0.4\n1 -0.2\n-0.300001\n-0.3\n-0.299999\n-0.2\n'
        self.assertEqual(self.run_solution(50,raw,['int']*4),[[0],[0],[1],[1]])
        self.assertEqual(self.run_solution(49,'2 1\n0 -0.4\n1 -0.2\n',['int','float']),[[0],[-0.3,0]])

    def test_bce_tiny_epsilon_against_independent_decimal_oracle(self):
        with localcontext() as ctx:
            ctx.prec=70
            eps=Decimal('1.000033e-12')
            wrong_loss=float(-eps.ln())
            correct_loss=float(-(Decimal(1)-eps).ln())
        for y,p in ((0,1),(1,0)):
            with self.subTest(y=y):
                output=self.run_solution(53,f'1 1 1.000033e-12\n{y} {p}\n0 1\n')[0]
                self.assertTrue(math.isclose(output[0],wrong_loss,abs_tol=1e-9,rel_tol=1e-11),(output[0],wrong_loss))
                self.assertTrue(math.isclose(output[1],correct_loss,abs_tol=1e-23,rel_tol=1e-11),(output[1],correct_loss))

    def test_all_twenty_topics_exist(self):
        for pid in range(39,59):
            folder='05_machine_learning' if pid<=50 else '06_neural_networks'
            for name in ('README.md','cases.json','exercise.py'):
                self.assertTrue((ROOT/'chapters'/folder/'problems'/f'P{pid:03}'/name).is_file())
            self.assertTrue((ROOT/'solutions'/f'P{pid:03}.py').is_file())
            self.assertTrue((ROOT/'solutions'/f'P{pid:03}.md').is_file())

    def test_convolution_and_transpose_match_explicit_linear_operator(self):
        # 独立构造9×20线性矩阵A，坐标条件决定每个输入像素的系数。
        h,w,kh,kw,s,p=4,5,2,3,2,1
        kernel=[[1,-2,3],[4,0,-1]]
        x=[j%7-3 for j in range(20)]
        u=[2,-1,3,0,1,-2,4,1,-1]
        matrix=[]
        for oi in range(3):
            for oj in range(3):
                coeff=[]
                for xi in range(h):
                    for xj in range(w):
                        a=xi-oi*s+p;b=xj-oj*s+p
                        coeff.append(kernel[a][b] if 0<=a<kh and 0<=b<kw else 0)
                matrix.append(coeff)
        matrix_output=[sum(a*t for a,t in zip(r,x)) for r in matrix]
        matrix_transpose=[sum(matrix[i][j]*u[i] for i in range(9)) for j in range(20)]
        raw='4 5 2 3 2 1\n'+'\n'.join(' '.join(map(str,x[i:i+5])) for i in range(0,20,5))+'\n1 -2 3\n4 0 -1\n'
        forward=[v for r in self.run_solution(55,raw) for v in r]
        traw='3 3 2 3 2 1\n'+'\n'.join(' '.join(map(str,u[i:i+3])) for i in range(0,9,3))+'\n1 -2 3\n4 0 -1\n'
        transpose=[v for r in self.run_solution(57,traw) for v in r]
        self.assertEqual(forward,matrix_output)
        self.assertEqual(transpose,matrix_transpose)
        self.assertEqual(sum(a*b for a,b in zip(forward,u)),sum(a*b for a,b in zip(x,transpose)))

    def test_gan_alternating_updates_match_finite_difference(self):
        def softplus(t):
            return max(t,0)+math.log1p(math.exp(-abs(t)))
        for xr,z,a,g,w,b,ld,lg in [(1,1,0,0,0,0,1,1),(.8,-1.2,.3,-.1,.5,.2,.1,.2)]:
            fake=a*z+g
            def dloss(params):
                return softplus(-(params[0]*xr+params[1]))+softplus(params[0]*fake+params[1])
            def derivative(function,params,j):
                plus=params[:];minus=params[:]
                plus[j]+=1e-5;minus[j]-=1e-5
                return (function(plus)-function(minus))/2e-5
            wd=w-ld*derivative(dloss,[w,b],0)
            bd=b-ld*derivative(dloss,[w,b],1)
            def gloss(params):
                return softplus(-(wd*(params[0]*z+params[1])+bd))
            anew=a-lg*derivative(gloss,[a,g],0)
            gnew=g-lg*derivative(gloss,[a,g],1)
            output=self.run_solution(58,' '.join(map(str,(xr,z,a,g,w,b,ld,lg)))+'\n')
            for actual,expected in zip(output[0]+output[1],[dloss([w,b]),gloss([a,g]),anew,gnew,wd,bd]):
                self.assertAlmostEqual(actual,expected,places=8)

    def test_softmax_translation_and_row_normalization(self):
        first=self.run_solution(52,'2 3\n-2 0 3\n5 -1 2\n')
        shifted=self.run_solution(52,'2 3\n98 100 103\n-95 -101 -98\n')
        for a,b in zip(first,shifted):
            self.assertAlmostEqual(sum(a),1,places=10)
            for x,y in zip(a,b):
                self.assertAlmostEqual(x,y,places=10)

    def test_network_update_uses_independent_loss_gradient(self):
        # 由数值导数构造期望更新，未调用参考解的梯度函数。
        samples=[(1,[1,2]),(0,[-2,1])]
        params=[0.3,-0.2,0.1]
        def loss(p):
            total=0
            for y,x in samples:
                z=sum(a*b for a,b in zip(p[:2],x))+p[2]
                total+=max(z,0)+math.log1p(math.exp(-abs(z)))-y*z
            return total/2
        out=self.run_solution(54,'2 2 0.2\n1 1 2\n0 -2 1\n0.3 -0.2\n0.1\n')
        self.assertAlmostEqual(out[0][0],loss(params),places=9)
        updated=out[1]+out[2]
        for j in range(3):
            p=params[:];m=params[:]
            p[j]+=1e-5;m[j]-=1e-5
            numerical=(loss(p)-loss(m))/2e-5
            self.assertAlmostEqual(updated[j],params[j]-.2*numerical,places=8)

    def test_cart_more_than_one_level_and_no_gain(self):
        train='6 1 3 2\n0 0\n0 1\n1 2\n1 3\n0 4\n0 5\n-1\n2.5\n5\n'
        self.assertEqual(self.run_solution(50,train),[[0],[1],[0]])
        xor='4 2 2 8\n0 0 0\n1 0 1\n1 1 0\n0 1 1\n0 1\n1 0\n'
        self.assertEqual(self.run_solution(50,xor),[[0],[0]])

    def test_best_split_matches_independent_exact_enumeration(self):
        # 四个不同点的全部16种二分类标签，精确分数检验最优阈值。
        for mask in range(16):
            labels=[(mask>>j)&1 for j in range(4)]
            def impurity(part):
                p=Fraction(sum(part),len(part))
                return 2*p*(1-p)
            scores=[Fraction(k,4)*impurity(labels[:k])+Fraction(4-k,4)*impurity(labels[k:]) for k in (1,2,3)]
            best=min(range(3),key=lambda j:scores[j])
            raw='4 1\n'+'\n'.join(f'{y} {j}' for j,y in enumerate(labels))+'\n'
            output=self.run_solution(49,raw,['int','float'])
            self.assertEqual(output[0],[0])
            self.assertEqual(output[1][0],best+0.5)
            self.assertAlmostEqual(output[1][1],float(scores[best]))

    def test_logistic_gradient_matches_finite_difference(self):
        samples=[(0,[1,-2]),(1,[3,0.5]),(1,[-1,2])]
        w=[0.2,-0.4]
        b=0.3
        def loss(params):
            value=0
            for y,x in samples:
                z=sum(a*t for a,t in zip(params[:2],x))+params[2]
                value+=max(z,0)+math.log1p(math.exp(-abs(z)))-y*z
            return value/3
        output=self.run_solution(46,'3 2\n0 1 -2\n1 3 0.5\n1 -1 2\n0.2 -0.4\n0.3\n')
        self.assertAlmostEqual(output[0][0],loss(w+[b]),places=10)
        gradient=output[1]+output[2]
        for j in range(3):
            plus=w+[b]; minus=w+[b]
            plus[j]+=1e-5; minus[j]-=1e-5
            self.assertAlmostEqual(gradient[j],(loss(plus)-loss(minus))/2e-5,places=7)

    def test_kmeans_sse_nonincreasing_and_empty_cluster(self):
        # 独立算最终SSE，对1..5轮数各跑一次而非调用答案内部函数。
        points=[0,1,4,7,10]
        initial=[0,2,100]
        previous=sum(min((x-c)**2 for c in initial) for x in points)
        for steps in range(1,6):
            output=self.run_solution(44,f'5 1 3 {steps} 0\n0\n1\n4\n7\n10\n0\n2\n100\n')
            centers=[r[0] for r in output[:-1]]
            labels=[int(v) for v in output[-1]]
            self.assertEqual(centers[2],100)
            current=sum((x-centers[k])**2 for x,k in zip(points,labels))
            self.assertLessEqual(current,previous+1e-10)
            previous=current

    def test_kmeans_large_exact_distance_tie(self):
        # 两个距离平方均为2*99.9²=19960.02，应选择小索引。
        body='0.1 0.1\n100 100\n-99.8 -99.8\n'
        with self.subTest(pid=42):
            self.assertEqual(self.run_solution(42, '1 2 2\n'+body, ['int']), [[0]])
        with self.subTest(pid=44):
            self.assertEqual(self.run_solution(44, '1 2 2 1 0\n'+body, ['float', 'float', 'int']), [[0.1,0.1],[-99.8,-99.8],[0]])

    def test_kmeans_exact_tolerance_boundary(self):
        # 低索引中心比最小距离分别多10^-12、4*10^-12；前者含边界平票。
        for center, label in (('0.000001', 0), ('0.000002', 1)):
            with self.subTest(center=center):
                body=f'0\n{center}\n0\n'
                self.assertEqual(self.run_solution(42, '1 1 2\n'+body, ['int']), [[label]])
                wanted=[[0],[0],[0]] if label == 0 else [[0.000002],[0],[1]]
                self.assertEqual(self.run_solution(44, '1 1 2 1 0\n'+body, ['float','float','int']), wanted)

    def test_kmeans_exact_center_update_and_stopping_boundary(self):
        # 首轮中心0.1、0.6，最大变化恰好0.3，因此停止；多走一轮会变成0.2、0.75。
        raw='4 1 2 10 0.3\n0.1\n0.3\n0.4\n1.1\n0.1\n0.3\n'
        self.assertEqual(self.run_solution(44, raw, ['float','float','int']), [[0.1],[0.6],[0,0,1,1]])


if __name__=='__main__':
    unittest.main()
