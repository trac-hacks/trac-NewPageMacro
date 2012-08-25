trac-NewPageMacro
=================

A little macro you can insert into your wiki pages which will let you create a new page from a template

Example Usage:

[[NewPage(parent=wiki/projects,template=ProjectTemplate,placeholder=My new project,button=New Project)]]

If you need more than one in a single page... provide and id:

[[NewPage(id=projects,parent=wiki/projects,template=ProjectTemplate,placeholder=My new project,button=New Project)]]
