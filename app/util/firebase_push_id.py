# pylint: disable=too-few-public-methods
"""Firebase Push Id Generator"""

import random
import time
import numpy


class PushID:
    """ PushID class """
    # Modeled after base64 web-safe chars, but ordered by ASCII.
    PUSH_CHARS = ('-0123456789'
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                  '_abcdefghijklmnopqrstuvwxyz')

    def __init__(self):

        # Timestamp of last push, used to prevent local collisions if you
        # pushtwice in one ms.
        self.last_push_time = 0

        # We generate 72-bits of randomness which get turned into 12
        # characters and appended to the timestamp to prevent
        # collisions with other clients.  We store the last characters
        # we generated because in the event of a collision, we'll use
        # those same characters except "incremented" by one.
        self.last_rand_chars = numpy.empty(12, dtype=int)

    def next_id(self):
        """ the method generates the next fancy_id """
        now = int(time.time() * 1000)
        duplicate_time = (now == self.last_push_time)
        self.last_push_time = now
        time_stamp_chars = numpy.empty(8, dtype=str)

        for i in range(7, -1, -1):
            time_stamp_chars[i] = self.PUSH_CHARS[now % 64]
            now = int(now / 64)

        if now != 0:
            raise ValueError('We should have converted the entire timestamp.')

        uid = ''.join(time_stamp_chars)

        if not duplicate_time:
            for i in range(12):
                self.last_rand_chars[i] = int(random.random() * 64)
        else:
            # If the timestamp hasn't changed since last push, use the
            # same random number, except incremented by 1.
            for i in range(11, -1, -1):
                if self.last_rand_chars[i] == 63:
                    self.last_rand_chars[i] = 0
                else:
                    break
            self.last_rand_chars[i] += 1

        for i in range(12):
            uid += self.PUSH_CHARS[self.last_rand_chars[i]]

        if len(uid) != 20:
            raise ValueError('Length should be 20.')
        return uid
