import pytest
import yaml


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
#为测试用例添加Mark标签
    #
    # for item in items:
    #     if 'add' in item.nodeid:
    #         item.add.marker(pytest.mark.add)
    #     if 'mutl' in item.nodeid:
    #         item.add.marker(pytest.mark.mutl)
    #     if 'subt' in item.nodeid:
    #         item.add.marker(pytest.mark.subt)
    #     if 'div' in item.nodeid:
    #         item.add.marker(pytest.mark.div)


#用例公共初始化部分
@pytest.fixture(scope="session")
def cal_begin():
    print("setup,初始化")
    yield

    print("teardown，环境恢复")


def pytest_addoption(parser):
    mygroup=parser.getgroup('hogwarts')
    mygroup.addoption('--env',
                      default = 'test',
                      dest='env',
                      help='set your env')


@pytest.fixture(scope='session')
def openenv(request):
    myenv=request.config.getoption('--env',default='test')
    if myenv =='test':
        datapath = 'cal_testing/testing_data/data_test.yml'

    if myenv =='dev':
        datapath = 'cal_testing/testing_data/data_dev.yml'

    if myenv == 'st':
        datapath = 'cal_testing/testing_data/data_st.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv,datas