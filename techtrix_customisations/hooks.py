from . import __version__ as app_version

app_name = "techtrix_customisations"
app_title = "Techtrix Customisations"
app_publisher = "TNS"
app_description = "Techtrix Customisations"
app_email = "furqan.79000@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/techtrix_customisations/css/techtrix_customisations.css"
# app_include_js = "/assets/techtrix_customisations/js/techtrix_customisations.js"

# include js, css files in header of web template
# web_include_css = "/assets/techtrix_customisations/css/techtrix_customisations.css"
# web_include_js = "/assets/techtrix_customisations/js/techtrix_customisations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "techtrix_customisations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Company" : "public/js/company.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "techtrix_customisations.utils.jinja_methods",
# 	"filters": "techtrix_customisations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "techtrix_customisations.install.before_install"
# after_install = "techtrix_customisations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "techtrix_customisations.uninstall.before_uninstall"
# after_uninstall = "techtrix_customisations.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "techtrix_customisations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Stock Entry": {
# 		"on_cancel": "techtrix_customisations.events.stock_entry.check_if_product_customisation_exist"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"techtrix_customisations.tasks.all"
# 	],
# 	"daily": [
# 		"techtrix_customisations.tasks.daily"
# 	],
# 	"hourly": [
# 		"techtrix_customisations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"techtrix_customisations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"techtrix_customisations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "techtrix_customisations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "techtrix_customisations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "techtrix_customisations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"techtrix_customisations.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
