from alfred.modules.api.a_base_module import ABaseModule

{%- set class_name = cookiecutter.package_name  |
             replace('_', ' ') |
             title() |
             replace(' ', '') %}

class {{ class_name }}(ABaseModule):
    def callback(self):
        pass

    def construct_view(self):
        h1 = AHeading(1, "{{ class_name }}")
        self.add_component(h1)
