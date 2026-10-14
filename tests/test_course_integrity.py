"""完整课程的结构、样例、练习状态与本地链接验收。"""
import ast
from collections import Counter
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

from check import compare_output

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IDS = {f'P{i:03}' for i in range(1,81)} | {f'M{i:02}{letter}' for i in range(1,5) for letter in 'AB'}
EXPECTED_COUNTS = {'01':14,'02':8,'03':8,'04':8,'05':12,'06':8,'07':12,'08':6,'09':4,'M01':2,'M02':2,'M03':2,'M04':2}


def materials():
    paths = list((ROOT/'chapters').glob('*/problems/*/cases.json')) + list((ROOT/'exams').glob('mock*/*/cases.json'))
    return [(p,json.loads(p.read_text(encoding='utf-8'))) for p in sorted(paths)]


class CourseIntegrity(unittest.TestCase):
    def test_exact_ids_and_chapter_counts(self):
        data=materials()
        self.assertEqual(len(data),88)
        self.assertEqual({d['id'] for p,d in data},EXPECTED_IDS)
        self.assertEqual(Counter(d['chapter'] for p,d in data),EXPECTED_COUNTS)
        for p,d in data:
            self.assertEqual(p.parent.name,d['id'])

    def test_all_required_materials_and_independent_code(self):
        for p,d in materials():
            pid=d['id']
            with self.subTest(pid=pid):
                for required in [p.parent/'README.md',p.parent/'exercise.py',ROOT/'solutions'/f'{pid}.py',ROOT/'solutions'/f'{pid}.md']:
                    self.assertTrue(required.is_file(),str(required))
                tree=ast.parse((ROOT/'solutions'/f'{pid}.py').read_text(encoding='utf-8'))
                for node in ast.walk(tree):
                    if isinstance(node,(ast.Import,ast.ImportFrom)):
                        names=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module or '']
                        self.assertFalse(any(name.startswith('solutions') or re.fullmatch(r'[PM]\d+.*',name) for name in names),names)

    def test_cases_unique_complete_and_shape_valid(self):
        total=0
        for p,d in materials():
            with self.subTest(pid=d['id']):
                self.assertIn(d['mode'],['text','int','float'])
                self.assertIn(d['requires'],[[],['numpy']])
                cases=d['cases']; total+=len(cases)
                self.assertGreaterEqual(len(cases),5)
                self.assertEqual(len({c['name'] for c in cases}),len(cases))
                for c in cases:
                    self.assertIsInstance(c['input'],str)
                    self.assertIsInstance(c['expected'],str)
                    self.assertTrue(c['name'])
                    ok,reason=compare_output(c['expected'],c['expected'],d['mode'],c.get('line_modes'))
                    self.assertTrue(ok,reason)
        self.assertGreaterEqual(total,440)

    def test_first_sample_matches_real_case(self):
        for p,d in materials():
            text=(p.parent/'README.md').read_text(encoding='utf-8')
            blocks=re.findall(r'```text[ \t]*\r?\n(.*?)\r?\n```',text,re.S)
            with self.subTest(pid=d['id']):
                self.assertGreaterEqual(len(blocks),2)
                self.assertEqual(blocks[0].strip(),d['cases'][0]['input'].strip())
                self.assertEqual(blocks[1].strip(),d['cases'][0]['expected'].strip())

    def test_problem_teaching_sections_and_solution_sections(self):
        for p,d in materials():
            text=(p.parent/'README.md').read_text(encoding='utf-8')
            solution=(ROOT/'solutions'/f'{d["id"]}.md').read_text(encoding='utf-8')
            with self.subTest(pid=d['id']):
                for pattern in ['输入','输出','手算']:
                    self.assertIn(pattern,text)
                for level in [1,2,3]:
                    self.assertRegex(text,fr'提示\s*{level}')
                self.assertIn('复杂度',solution)
                self.assertIn('易错',solution)
                self.assertRegex(text,r'\]\(https://[^)]+\)')
                self.assertRegex(solution,r'\]\(https://[^)]+\)')

    def test_exercises_still_unfinished_and_do_not_import_answers(self):
        for p,d in materials():
            tree=ast.parse((p.parent/'exercise.py').read_text(encoding='utf-8'))
            with self.subTest(pid=d['id']):
                self.assertTrue(any(isinstance(node,ast.Raise) and isinstance(node.exc,ast.Call) and isinstance(node.exc.func,ast.Name) and node.exc.func.id=='NotImplementedError' for node in ast.walk(tree)))
                for node in ast.walk(tree):
                    if isinstance(node,(ast.Import,ast.ImportFrom)):
                        names=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module or '']
                        self.assertFalse(any('solutions' in name or re.fullmatch(r'[PM]\d+.*',name) for name in names))

    def test_chapter_tutorials_and_exam_navigation(self):
        for folder in sorted((ROOT/'chapters').iterdir()):
            if not folder.is_dir(): continue
            tutorial=folder/'README.md'
            self.assertTrue(tutorial.is_file())
            text=tutorial.read_text(encoding='utf-8')
            self.assertGreater(len(text),1000)
            for p in folder.glob('problems/*/cases.json'):
                self.assertIn(f'problems/{p.parent.name}/README.md',text)
        for i in range(1,5):
            self.assertTrue((ROOT/'exams'/f'mock{i:02}'/'README.md').is_file())

    def test_progress_has_exactly_88_rows(self):
        text=(ROOT/'PROGRESS.md').read_text(encoding='utf-8')
        ids=re.findall(r'^- \[[ xX]\] \[([PM]\d+(?:[AB])?) ',text,re.M)
        self.assertEqual(len(ids),88)
        self.assertEqual(set(ids),EXPECTED_IDS)
        self.assertIn('复习',text)

    def test_navigation_has_no_stage_placeholder(self):
        for path in [ROOT/'README.md',ROOT/'docs/START_HERE.md']:
            text=path.read_text(encoding='utf-8')
            self.assertNotRegex(text,r'后续.*(?:生成|参考解)|尚未提供正式题目|基础工具阶段')
            self.assertIn('P001/README.md',text)
        for filename in ['MISTAKES.md','REFERENCES.md','MAINTAINING.md']:
            self.assertTrue((ROOT/'docs'/filename).is_file())

    def test_course_local_markdown_links_resolve(self):
        paths=[ROOT/'README.md',ROOT/'PROGRESS.md']
        paths+=list((ROOT/'docs').glob('*.md'))
        paths+=list((ROOT/'chapters').rglob('README.md'))
        paths+=list((ROOT/'exams').rglob('README.md'))
        paths+=list((ROOT/'solutions').glob('*.md'))
        for path in paths:
            text=path.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
                if re.match(r'https?://|mailto:|#',target): continue
                target=unquote(target.split('#',1)[0].strip('<>'))
                with self.subTest(file=str(path.relative_to(ROOT)),target=target):
                    self.assertTrue((path.parent/target).exists(),target)


if __name__=='__main__': unittest.main()
