from django.shortcuts import HttpResponse
from django.conf.urls import url
from django.forms import ModelForm
from stark.service import router
from app01 import models
class UserInfoModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        error_messages = {
            'name':{
                'required':'用户名不能为空'
            }
        }


class UserInfoConfig(router.StarkConfig):
    list_display = ['id', 'name','email']
    show_add_btn = True
    model_form_class = UserInfoModelForm

router.site.register(models.UserInfo, UserInfoConfig)


class RoleConfig(router.StarkConfig):
    list_display = ['id', 'name']

router.site.register(models.Role, RoleConfig)  # StarkConfig(Role)


class UserTypeConfig(router.StarkConfig):
    list_display = ['id', 'title']

router.site.register(models.UserType, UserTypeConfig)  # StarkConfig(Role)



class HostModelForm(ModelForm):
    class Meta:
        model = models.Host
        fields = ['id','hostname','ip','port']
        error_messages = {
            'hostname':{
                'required':'主机名不能为空',
            },
            'ip':{
                'required': 'IP不能为空',
                'invalid': 'IP格式错误',
            }

        }


class HostConfig(router.StarkConfig):
    def ip_port(self,obj=None,is_header=False):
        if is_header:
            return '自定义列'
        return "%s:%s" %(obj.ip,obj.port,)

    list_display = ['id','hostname','ip','port',ip_port]
    # get_list_display

    show_add_btn = True
    # get_show_add_btn

    model_form_class = HostModelForm
    # get_model_form_class


    def extra_url(self):
        urls = [
            url('^report/$',self.report_view)
        ]
        return urls

    def report_view(self,request):
        return HttpResponse('自定义报表')

    def delete_view(self,request,nid,*args,**kwargs):
        if request.method == "GET":
            return render(request,'my_delete.html')
        else:
            self.model_class.objects.filter(pk=nid).delete()
            return redirect(self.get_list_url())

router.site.register(models.Host,HostConfig)

