from presenter.cli_presenter import CliPresenter
from presenter.presenter import Presenter


class PresenterFactory():
    @staticmethod
    def get_presenter() -> Presenter:
        return CliPresenter()
