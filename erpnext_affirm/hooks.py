# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_affirm"
app_title = "ERPNext Affirm Integration"
app_publisher = "Neil Lasrado"
app_description = "Affirm (https://www.affirm.com) Integration for ERPNext"
app_icon = "octicon octicon-radio-tower"
app_color = "light blue"
app_email = "neil@digithinkit.com"
app_license = "GPL"

web_include_css = [
	"/assets/erpnext_affirm/css/awc_checkout.css?v=%s" % app_version
]

doctype_js = {
	"Sales Order": "public/js/capture_affirm_payment.js"
}
