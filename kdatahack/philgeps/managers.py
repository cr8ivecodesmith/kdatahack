from django.db import models


class OrganizationManager(models.Manager):
    def import_csv_data(self, csvfile):
        # TODO: Implement this method.
        pass


class BidInformationManager(models.Manager):
    def import_csv_data(self, csvfile):
        # TODO: Implement this method.
        pass


class BidLineItemManager(models.Manager):
    def import_csv_data(self, csvfile):
        # TODO: Implement this method.
        pass


class AwardsManager(models.Manager):
    def import_csv_data(self, csvfile):
        # TODO: Implement this method.
        pass


class BiddersListManager(models.Manager):
    def import_csv_data(self, csvfile):
        # TODO: Implement this method.
        pass
