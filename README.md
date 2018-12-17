jenkins_job_dsl_exec
====================

[![Build Status](https://travis-ci.com/meierw/jenkins-job-dsl-exec.svg?branch=master)](https://travis-ci.com/meierw/jenkins-job-dsl-exec)

Ansible role, that creates, executes and then deletes a temporary Jenkins job containing a Job DSL script.

Requirements
------------

* A Jenkins service, with the `Job DSL` plugin installed.
* The ability to execute [jenkins_script](https://docs.ansible.com/ansible/2.5/modules/jenkins_script_module.html) against said Jenkins service.

Role Variables
--------------

```yaml
jenkins_job_dsl_url: http://localhost:8080
jenkins_job_dsl_user: admin
jenkins_job_dsl_password: admin
```
The URL, username and password for authenticating with Jenkins. Will be used to execute `jenkins_script`.

-------
```yaml
jenkins_job_dsl_temp_job_name: C4lpe7GMX8S0pdZV6RWbKAkBfKWCPAOgAL9MGL03
```
The name of the temporary job, which will be used for the DSL script execution.
Should keep this as a complicated string of characters, to avoid collision with actual job names.

-------
```yaml
jenkins_job_dsl_content: |
    job('dsl-example-job') {
        steps {
            shell('echo Hello world!')
        }
    }
```
The DSL script, that will be run. You can specify it inline like in the example, 
or us something like `jenkins_job_dsl_content: "{{ lookup('file', 'files/myDslScript.groovy') }}"` if you want your playbook to be more neat.

> During runtime, `jenkins_job_dsl_content` is fed into a groovy script, like so - `builder.setScriptText('''{{ jenkins_job_dsl_content }}''')`.
This means that if your `jenkins_job_dsl_content` contains a `'''multiline string in three single quotes'''`, it will break things.
Use a `"""multiline string in three double quotes"""` instead.

-------
```yaml
jenkins_job_dsl_temp_job_run: true
```
Should the newly created temporary job be run.
You may want to disable this if you have a different plan for when or how you want to run it.

-------
```yaml
jenkins_job_dsl_temp_job_delete: true
```
Should the temporary job be deleted after running it.
You may want to disable this, if you're not getting the desired result and want to check out the build log in Jenkins.
Does nothing if `jenkins_job_dsl_temp_job_run is false`.

-------
```yaml
jenkins_job_dsl_temp_job_running_checks: 10
```
How many times should the role check, if the job has stopped running, before deleting it.
The role performs a check every second, so this amount is also the checking timeout limit in seconds.
Does nothing if `jenkins_job_dsl_temp_job_delete is false`.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - { role: meierw.jenkins_job_dsl_exec }
```

License
-------

MIT

Author Information
------------------

* _Author:_ [Walter Meier](mailto:valters.meirens@gmail.com)
