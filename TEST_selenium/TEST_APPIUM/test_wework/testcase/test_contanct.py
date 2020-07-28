import pytest
import yaml

from TEST_APPIUM.test_wework.basepage.app import APP

with open('../testdatas/member_data.yml',encoding='utf-8') as f:
    datas=yaml.safe_load(f)
    myids_add=datas['add'].keys()
    mydatas_add=datas['add'].values()

    myids_del=datas['del'].keys()
    mydatas_del=datas['del'].values()

class TestContact:

    def setup_class(self):
        self.app=APP()
        self.main=self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('name,phonenumber,gender', mydatas_add, ids=myids_add)
    def test_addcontanct(self,name,gender,phonenumber):
        print(f'开始添加成员{name}')
        mypage=self.main.goto_contancs().add_contanct().add_member().\
            set_name(name).set_gender(gender).\
            set_phonenumber(phonenumber).click_save()
        text=mypage.get_toast()
        assert '成功' in text
        self.app.back()

    @pytest.mark.parametrize('name', mydatas_del, ids=myids_del)
    def test_delcontanct(self,name):
        print(f'开始删除成员{name}')
        mypage=self.main.goto_contancs().\
            search_contanct().goto_search(name).\
            goto_memberlist(name).goto_edit().\
            goto_delmember().del_member()

        num=mypage.memberlist_after(name)
#        assert num ==1
        self.app.back()


