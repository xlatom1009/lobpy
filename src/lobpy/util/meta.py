__author__ = "nap"
__copyright__ = "nap"
__license__ = "MIT"


class EnforcedAttributeMeta(type):
    def __call__(cls, *args, **kwargs):
        class_object = type.__call__(cls, *args, **kwargs)
        class_object._check_required_attributes()
        return class_object
