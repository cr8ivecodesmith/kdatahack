from messytables import (CSVTableSet, headers_guess, headers_processor, offset_processor,
                         type_guess, types_processor)

class CSVData(object):

    def __init__(self, file_object, headers=None, offset=None, types=None):
        table_set = CSVTableSet(file_object)
        self._row_set = table_set.tables[0]

        self.headers = self.set_headers(headers)
        self.offset = self.set_offset(offset)
        self.types = self.set_types(types)

        self._row_set.register_processor(headers_processor(self.headers))
        self._row_set.register_processor(offset_processor(self.offset))
        self._row_set.register_processor(types_processor(self.types))

        self.items = self._row_set

    def set_headers(self, headers=None):
        if not headers:
            headers = headers_guess(self._row_set.sample)[1]
        return headers

    def set_offset(self, offset=None):
        if not offset:
            offset = headers_guess(self._row_set.sample)[0] + 1
        return offset

    def set_types(self, types=None):
        if not types:
            types = type_guess(self._row_set.sample, strict=True)
        return types