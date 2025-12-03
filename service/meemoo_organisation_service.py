class MeemooOrganisationService:
    def get_partners_by_ids(self, ids: set[str]):
        # Contact organisations api, retrieve id's of organisations that are partnered
        not_partners = {"NotAPartner1", "NotAPartner2"}
        return ids.difference(not_partners)
