import abc

class AbstractBaseClass(object):

    @abc.abstractmethod
    def method(self, string):
        """Print a string
        """
