import random

from monosloth.contracts import Command


class Inspire(Command):

    def set_quotes(self, *inspirations):
        """Set inspirational quotes.

        :param inspirations: The inspirational messages.

        """
        self.inspirations = inspirations

    def usage(self):
        """The command instruction."""
        return 'inspire'

    def run(self, input, output):
        """Invoke a command.

        :param input: An input interface.
        :param output: An output interface.

        """
        count = len(self.inspirations) - 1
        index = random.randrange(0, count)
        
        output.info(self.inspirations[index])
