class MeemooOrganisationService:
    def get_partners_by_ids(self, organisation_id: set[str]):
        """
        :param organisation_id: organisation id's
        :return: id's of organisations that are partnered
        """
        # Contact organisations api, retrieve id's of organisations that are partnered
        not_partners = {"NotAPartner1", "NotAPartner2"}
        return organisation_id.difference(not_partners)
