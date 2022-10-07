
class Kit():
    """Docstring for Kit. """

    kit = []

    def __init__(self):
        """TODO: to be defined. """
        pass
        
    def rest_all(self, duration: int):
        """TODO: Docstring for rest_all.

        :duration: TODO
        """
        duration = int(duration)
        for perc in self.kit:
            perc.set_rest(duration)
