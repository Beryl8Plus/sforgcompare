from django.db import models

class Job(models.Model):
	created_date = models.DateTimeField(null=True,blank=True)
	finished_date = models.DateTimeField(null=True,blank=True)
	compare_result_html = models.TextField(null=True,blank=True)
	api_choice = models.CharField(max_length=255,blank=True)
	email_result = models.BooleanField()
	email = models.CharField(max_length=255,blank=True)
	status = models.CharField(max_length=255, blank=True)
	error = models.TextField(blank=True)

	def sorted_orgs(self):
		return self.org_set.order_by('org_number')

class Org(models.Model):
	job = models.ForeignKey(Job, blank=True, null=True)
	org_number = models.PositiveSmallIntegerField()
	access_token = models.CharField(max_length=255)
	instance_url = models.CharField(max_length=255)
	org_id = models.CharField(max_length=255)
	org_name = models.CharField(max_length=255, blank=True)
	username = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, blank=True)
	error = models.TextField(blank=True)

	def sorted_component_types(self):
		return self.componenttype_set.order_by('name')

class ComponentType(models.Model):
	org = models.ForeignKey(Org)
	name = models.CharField(max_length=255)

	def sorted_components(self):
		return self.component_set.order_by('name')

	def org_name(self):
		return self.org.org_name

class Component(models.Model):
	component_type = models.ForeignKey(ComponentType)
	name = models.CharField(max_length=255)
	content = models.TextField(blank=True, null=True)