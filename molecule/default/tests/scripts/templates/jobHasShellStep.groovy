print Jenkins.get().getItemByFullName('{{ new_job_name }}').getBuilders()
	.find { it.class == hudson.tasks.Shell } ? true : false