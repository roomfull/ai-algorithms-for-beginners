"""P059–P080: hand-computed cases plus independent enumeration/numerical oracles."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, product
import importlib.util
import json
import math
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from check import compare_output


class SystemAlgorithmsTests(unittest.TestCase):
    modules={}

    def run_solution(self,pid,raw):
        path=ROOT/'solutions'/f'P{pid:03}.py'
        self.assertTrue(path.is_file(),f'缺少参考实现 P{pid:03}')
        if pid not in self.modules:
            spec=importlib.util.spec_from_file_location(f'system_{pid}',path)
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            self.modules[pid]=mod
        return self.modules[pid].solve(raw).strip()

    def floats(self,pid,raw):
        return [[float(x) for x in line.split()] for line in self.run_solution(pid,raw).splitlines()]

    def test_independent_cases(self):
        for pid in range(59,81):
            chapter='07_graphs' if pid<=70 else '08_compression' if pid<=76 else '09_distributed'
            path=ROOT/'chapters'/chapter/'problems'/f'P{pid:03}'/'cases.json'
            if not path.is_file():
                continue  # 分批生成；完整性测试保证最后不能漏题。
            data=json.loads(path.read_text(encoding='utf-8'))
            self.assertGreaterEqual(len(data['cases']),5)
            for c in data['cases']:
                with self.subTest(pid=pid,case=c['name']):
                    ok,reason=compare_output(self.run_solution(pid,c['input']),c['expected'],data['mode'],c.get('line_modes'))
                    self.assertTrue(ok,reason)

    def test_all_22_material_sets(self):
        for pid in range(59,81):
            chapter='07_graphs' if pid<=70 else '08_compression' if pid<=76 else '09_distributed'
            for name in ('README.md','exercise.py','cases.json'):
                self.assertTrue((ROOT/'chapters'/chapter/'problems'/f'P{pid:03}'/name).is_file())
            for suffix in ('py','md'):
                self.assertTrue((ROOT/'solutions'/f'P{pid:03}.{suffix}').is_file())

    def test_triangle_enumeration_all_five_vertex_graphs(self):
        edges=list(combinations(range(5),2))
        for bits in range(1<<len(edges)):
            chosen={e for k,e in enumerate(edges) if bits>>k&1}
            want=sum(all(tuple(sorted(e)) in chosen for e in combinations(vs,2)) for vs in combinations(range(5),3))
            raw=f'5 {len(chosen)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(chosen))
            self.assertEqual(int(self.run_solution(64,raw)),want)

    def test_components_bipartition_bfs_and_combined_independent_enumeration(self):
        n=4
        edges=list(combinations(range(n),2))
        for bits in range(1<<len(edges)):
            chosen=[e for k,e in enumerate(edges) if bits>>k&1]
            reach=[[i==j or tuple(sorted((i,j))) in chosen for j in range(n)] for i in range(n)]
            # Floyd传递闭包作为独立oracle，不使用BFS/DFS实现。
            distances=[[0 if i==j else 1 if reach[i][j] else 99 for j in range(n)] for i in range(n)]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        distances[i][j]=min(distances[i][j],distances[i][k]+distances[k][j])
            representative=[min(j for j in range(n) if distances[i][j]<99) for i in range(n)]
            roots=sorted(set(representative))
            labels=[roots.index(r) for r in representative]
            bip=int(any(all(color[u]!=color[v] for u,v in chosen) for color in product((0,1),repeat=n)))
            triangles=sum(all(tuple(sorted(e)) in chosen for e in combinations(vs,2)) for vs in combinations(range(n),3))
            tail=''.join(f'{u} {v}\n' for u,v in chosen)
            raw=f'{n} {len(chosen)}\n'+tail
            self.assertEqual(self.floats(62,raw),[[len(roots)],labels])
            self.assertEqual(int(self.run_solution(65,raw)),bip)
            self.assertEqual(self.floats(70,raw),[[len(roots),bip,triangles]])
            for start in range(n):
                wanted=[d if d<99 else -1 for d in distances[start]]
                self.assertEqual(self.floats(61,f'{n} {len(chosen)} {start}\n'+tail),[wanted])

    def test_msts_match_all_spanning_tree_subsets_with_negative_weights(self):
        n=4
        all_edges=[(u,v,(u*3+v)%7-3) for u,v in combinations(range(n),2)]
        for mask in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if mask>>i&1]
            totals=[]
            for subset in combinations(edges,n-1):
                seen={0}
                for _ in range(n):
                    for u,v,_ in subset:
                        if u in seen or v in seen:
                            seen.update((u,v))
                if len(seen)==n:
                    totals.append(sum(w for _,_,w in subset))
            expected=str(min(totals)) if totals else 'DISCONNECTED'
            raw=f'{n} {len(edges)}\n'+''.join(f'{u} {v} {w}\n' for u,v,w in edges)
            for pid in (66,67):
                self.assertEqual(self.run_solution(pid,raw),expected)

    def test_pagerank_transition_matrix_probability_mass(self):
        n=3
        # 包括无边、悬挂点、自环和一对多；用显式随机转移矩阵核验。
        for edges in ([],[(0,1)],[(0,0),(0,2),(2,1)],[(0,1),(1,2),(2,0)]):
            counts=[sum(u==i for u,v in edges) for i in range(n)]
            a=Fraction('0.8')
            p=[Fraction('0.2'),Fraction('0.3'),Fraction('0.5')]
            transition=[[Fraction(1,n) if counts[u]==0 else Fraction((u,v) in edges,counts[u]) for v in range(n)] for u in range(n)]
            expected=[float((1-a)/n+a*sum(p[u]*transition[u][v] for u in range(n))) for v in range(n)]
            raw=f'3 {len(edges)} 0.8\n'+''.join(f'{u} {v}\n' for u,v in edges)+'0.2 0.3 0.5\n'
            actual=self.floats(68,raw)[0]
            self.assertAlmostEqual(sum(actual),1,places=10)
            for x,y in zip(actual,expected):
                self.assertAlmostEqual(x,y,places=10)

    def test_pagerank_stop_l1_threshold_and_iteration_limit(self):
        self.assertEqual(self.floats(69,'2 1 0.5 0.25 5\n0 1\n'),[[1,1],[0.375,0.625]])
        self.assertEqual(self.floats(69,'2 1 0.5 0.249999 1\n0 1\n'),[[1,0],[0.375,0.625]])
        out=self.floats(69,'2 1 0.8 0.000001 100\n0 1\n')
        self.assertEqual(out[0][1],1)
        self.assertAlmostEqual(sum(out[1]),1,places=10)
        self.assertAlmostEqual(out[1][0],5/14,places=6)

    def test_pagerank_exact_decimal_stop_boundary(self):
        # 有理数首轮oracle：(.495,.505)，L1=1/100，避免二进制浮点误判。
        expected=[Fraction('0.495'),Fraction('0.505')]
        delta=sum(abs(p-Fraction(1,2)) for p in expected)
        self.assertEqual(delta,Fraction('0.010'))
        self.assertEqual(self.floats(69,'2 1 0.02 0.010 1\n0 1\n'),[[1,1],[0.495,0.505]])
        self.assertEqual(self.floats(69,'2 1 0.02 0.009999 1\n0 1\n'),[[1,0],[0.495,0.505]])

    def test_ratio_decimal_floor_and_deterministic_ties(self):
        for n,ratio in ((100,'0.29'),(10,'0.7'),(3,'0.5'),(4,'0'),(4,'1')):
            count=(n*Fraction(ratio)).numerator//(n*Fraction(ratio)).denominator
            out=self.floats(72,f'{n} {ratio}\n'+' '.join(['1']*n)+'\n')
            self.assertEqual(out[0],[0]*count+[1]*(n-count))
            self.assertEqual(out[1],[0]*count+[1]*(n-count))
        self.assertEqual(self.floats(73,'2 2 1\n0.1 0.2\n0.3 0\n'),[[1,0],[0.1,0.2]])

    def test_symmetric_quantization_exact_half_steps_and_error_bound(self):
        raw='9\n127 -127 0.5 1.5 2.5 -0.5 -1.5 -2.5 0\n'
        out=self.floats(74,raw)
        self.assertEqual(out,[[1],[127,-127,0,2,2,0,-2,-2,0],[127,-127,0,2,2,0,-2,-2,0]])
        # 0.3量化到127，使0.15对应63.5；浮点比值不可靠，必须精确ties-to-even。
        self.assertEqual(self.floats(74,'3\n0.3 0.15 -0.15\n')[1],[127,64,-64])
        value_tokens=('-0.37','0.23','0.11','-0.19','0')
        values=[Fraction(t) for t in value_tokens]
        out=self.floats(74,'5\n'+' '.join(value_tokens)+'\n')
        scale=float(max(map(abs,values))/127)
        self.assertTrue(all(-127<=q<=127 for q in out[1]))
        for x,dq in zip(values,out[2]):
            self.assertLessEqual(abs(float(x)-dq),scale/2+1e-11)
        self.assertEqual(self.floats(74,'2\n0 0\n'),[[1],[0,0],[0,0]])

    def test_affine_quantization_ties_round_before_zero_point_and_clipping(self):
        out=self.floats(75,'8 0.1 1\n0.05 0.15 0.25 -0.05 -0.15 -0.25 -100 100\n')
        self.assertEqual(out[0],[1,3,3,1,0,0,0,255])
        self.assertEqual(out[1],[0,0.2,0.2,0,-0.1,-0.1,-0.1,25.4])
        # 奇数zero_point能区分round(x/s)+zp与round(x/s+zp)。
        for t in ('0.05','0.15','0.25','-0.05','-0.15','-0.25'):
            wanted=max(0,min(255,round(Fraction(t)/Fraction('0.1'))+127))
            out=self.floats(75,f'1 0.1 127\n{t}\n')
            self.assertEqual(out[0],[wanted])
            self.assertLessEqual(abs(float(t)-out[1][0]),0.05+1e-12)

    def test_quant_error_storage_independent_formula(self):
        x=[1,-2,3]
        y=[1.5,-1,2]
        self.assertEqual(self.floats(76,'3\n1 -2 3\n1.5 -1 2\n'),[[0.75,1],[12,3]])

    def test_balanced_shards_cover_once_and_allow_empty(self):
        for n in range(9):
            for w in range(1,7):
                ranges=self.floats(77,f'{n} {w}\n')
                self.assertEqual(len(ranges),w)
                coverage=[i for a,b in ranges for i in range(int(a),int(b))]
                self.assertEqual(coverage,list(range(n)))
                sizes=[int(b-a) for a,b in ranges]
                self.assertLessEqual(max(sizes)-min(sizes),1)
                self.assertEqual(sizes,sorted(sizes,reverse=True))

    def test_simple_average_differs_from_sample_weighted_average(self):
        self.assertEqual(self.floats(78,'2 2\n1 3\n5 -1\n'),[[3,1]])
        self.assertEqual(self.floats(79,'2 2\n1 1 3\n3 5 -1\n'),[[4,0]])
        self.assertEqual(self.floats(79,'2 1\n0 999\n4 -2\n'),[[-2]])

    def test_microbatch_sync_sgd_matches_explicit_fullbatch_samples(self):
        # 每个样本提供一个二维梯度；手工分组局部均值再输入，不依赖任何答案。
        samples=[[1,2],[3,4],[-2,1],[0,5],[4,-2],[5,0]]
        groups=(((0,1),(2,)),((3,4,5),))
        params=[10,-3]
        raw='2 2 0.2\n10 -3\n'
        for worker in groups:
            raw+=f'{len(worker)}\n'
            for indices in worker:
                means=[sum(Fraction(samples[i][j]) for i in indices)/len(indices) for j in range(2)]
                raw+=f'{len(indices)} '+' '.join(str(float(v)) for v in means)+'\n'
        out=self.floats(80,raw)
        expected=[sum(row[j] for row in samples)/len(samples) for j in range(2)]
        for j in range(2):
            self.assertAlmostEqual(out[0][j],expected[j],places=10)
            self.assertAlmostEqual(out[1][j],params[j]-0.2*expected[j],places=10)
        # 空worker合法；零样本局部项不影响，且只更新一次。
        self.assertEqual(self.floats(80,'2 1 0.5\n4\n0\n2\n0 999\n2 6\n'),[[6],[1]])


if __name__=='__main__':
    unittest.main()
