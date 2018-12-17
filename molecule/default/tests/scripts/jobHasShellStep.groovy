print Jenkins.get().getItemByFullName('dsl-example-job').getBuilders()
	.find { it.class == hudson.tasks.Shell } ? true : false