import pytest
# class Test_Demo():
    # def test_demo(self):
    #     a = 5
    #     b = -1
    #     assert a != b
    #     print("我的第一个测试用例")

# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","liushixushiwoer","liangshuaige"])
# def test_add(a,b,expected):
#     assert add_function(a,b) == expected

# @pytest.mark.parametrize("a",[0, 1, 2])
# @pytest.mark.parametrize("b",[2, 3, 4])
# def test_foo(a,b):
#     print("测试数据组合: a->%s, b->%s" % (a,b))

# def setup_module():
#  print(
#  "\nsetup_module：整个test_module.py模块只执⾏⼀次"
#  )
# def teardown_module():
#  print(
#  "\nteardown_module：整个test_module.py模块只执⾏⼀次"
#  )
# def setup_function():
#  print("\nsetup_function：每个不在类中的⽤例开始前都会执⾏")
# def teardown_function():
#  print("\nteardown_function：每个不在类中的⽤例结束后都会执⾏")
# # 测试模块中的⽤例1
# def test_one():
#  print("正在执⾏测试模块----test_one")
# # 测试模块中的⽤例2
# def test_two():
#  print("正在执⾏测试模块----test_two")
# # 测试类
# class TestCase():
#  def setup_class(self):
#     print("\nsetup_class：所有⽤例执⾏之前")
#  def teardown_class(self):
#     print("\nteardown_class：所有⽤例执⾏之后")
#  def setup_method(self):
#     print("\nsetup_method: 每个⽤例开始前执⾏")
#  def teardown_method(self):
#     print("\nteardown_method: 每个⽤例结束后执⾏")
#  def setup(self):
#     print("\nsetup：每个⽤例开始前都会执⾏")
#  def teardown(self):
#     print("\nteardown：每个⽤例结束后都会执⾏")
#  def test_three(self):
#     print("\n正在执⾏测试类----test_three")
#  def test_four(self):
#     print("\n正在执⾏测试类----test_four")


# import yaml
# def step1():
#     print("打开浏览器")
# def step2():
#     print("注册新账号")
# def step3():
#     print("登录新账号")
# def steps(path):
#     with open(path) as f:
#         steps = yaml.safe_load(f)
#     for step in steps:
#         if "step1" in step:
#             step1()
#         elif "step2" in step:
#             step2()
#         elif "step3" in step:
#             step3()
# def test_foo():
#     steps("./steps.yml")
import random
@pytest.mark.flaky(reruns=6,reruns_delay=2)
def test_exampl():
    print(3)
    assert 1==-1
# def test_simple_assume():
#  pytest.assume(1 == -1)
#  pytest.assume(True)
#  pytest.assume(False)

# @pytest.mark.run(order=2)
# def test_foo():
#     assert True
#
# @pytest.mark.run(order=1)
# def test_bar():
#     assert True
#
# @pytest.mark.run(order=4)
# def test_ner():
#     assert True
#
# @pytest.mark.run(order=3)
# def test_dre():
#     assert True




