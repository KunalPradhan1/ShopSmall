# class CustomerRouter: 
#      """
#     A router to control all database operations on models in the
#     customers application.
#     """
#     route_app_labels = {'customers_app'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'customers'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'customers'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'customers'
#         return None


# class BusinessRouter:
#     """
#     A router to control all database operations on models in the
#     businesses application.
#     """
#     route_app_labels = {'businesses_app'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'businesses'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'businesses'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'businesses'
#         return None