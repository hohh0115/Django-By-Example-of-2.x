from django import forms
from django.utils.translation import gettext_lazy as _

class CouponApplyForm(forms.Form):
	"""docstring for CouponApplyForm"""
	code = forms.CharField(label=_('Coupon'))
