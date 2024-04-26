from enum import Enum


class Routes(str, Enum):
    SIGN_IN = '/sign_in'
    CHANGE_PASSWORD = '/user/settings/password/change'
    CREATE_REPO = '/user/repos'
    USER = '/user'

    @staticmethod
    def DELETE_REPO(user, name):
        return f'/repos/{user}/{name}'

    @staticmethod
    def GET_ALL_COMMITS(user, name):
        return f'/repos/{user}/{name}/commits'

    @staticmethod
    def CREATE_WEBHOOK(user, name):
        return f'/repos/{user}/{name}/hooks'

    @staticmethod
    def PUSH_WEBHOOK(user, name, id):
        return f'/repos/{user}/{name}/hooks/{id}/tests'

    @staticmethod
    def CREATE_ISSUE(user, name):
        return f'/repos/{user}/{name}/issues'

    @staticmethod
    def CREATE_WIKI(owner, repo):
        return f'/repos/{owner}/{repo}/wiki/new'

    @staticmethod
    def GET_WIKI(owner, repo, page_path):
        return f'/repos/{owner}/{repo}/wiki/page/{page_path}'

    @staticmethod
    def DELETE_WIKI(owner, repo, page_path):
        return f'/repos/{owner}/{repo}/wiki/page/{page_path}'

    @staticmethod
    def EDIT_WIKI(owner, repo, page_path):
        return f'/repos/{owner}/{repo}/wiki/page/{page_path}'

    @staticmethod
    def GET_ALL_WIKI(owner, repo):
        return f'/repos/{owner}/{repo}/wiki/pages'

    @staticmethod
    def GET_WIKI_REVISIONS(owner, repo, page_path):
        return f'/repos/{owner}/{repo}/wiki/revisions/{page_path}'

    @staticmethod
    def GET_WIKI_TREE(owner, repo):
        return f'/repos/{owner}/{repo}/wiki/tree'

    @staticmethod
    def LIST_BRANCH_PROTECTIONS(owner, repo):
        return f'/repos/{owner}/{repo}/branch_protections'

    @staticmethod
    def CREATE_BRANCH_PROTECTION(owner, repo):
        return f'/repos/{owner}/{repo}/branch_protections'

    @staticmethod
    def CREATE_BRANCH(owner, repo):
        return f'/repos/{owner}/{repo}/branches'

    @staticmethod
    def LIST_BRANCHES(owner, repo):
        return f'/repos/{owner}/{repo}/branches'

    @staticmethod
    def GET_BRANCH(owner, repo, branch_name):
        return f'/repos/{owner}/{repo}/branches/{branch_name}'

    @staticmethod
    def DELETE_BRANCH(owner, repo, branch_name):
        return f'/repos/{owner}/{repo}/branches/{branch_name}'

    @staticmethod
    def EDIT_BRANCH(owner, repo, branch_name):
        return f'/repos/{owner}/{repo}/branches/{branch_name}/rename'

    @staticmethod
    def DELETE_BRANCH_PROTECTION(owner, repo, name):
        return f'/repos/{owner}/{repo}/branch_protections/{name}'

    @staticmethod
    def EDIT_BRANCH_PROTECTION(owner, repo, name):
        return f'/repos/{owner}/{repo}/branch_protections/{name}'

    def __str__(self) -> str:
        return self.value
