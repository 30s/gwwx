from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException


class Wechat(View):

    def dispatch(self, *args, **kwargs):
        signature = self.request.GET.get('signature', '')
        timestamp = self.request.GET.get('timestamp', '')
        nonce = self.request.GET.get('nonce', '')

        try:
            check_signature(settings.TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            return HttpResponse(status=403)

        return super(Wechat, self).dispatch(*args, **kwargs)

    def get(self, request):
        echo_str = request.GET.get('echostr', '')
        return HttpResponse(echo_str)
