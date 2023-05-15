from typing import Dict


class Meta:

    def __init__(self, **kwargs):
        self.__page_no = kwargs.get('page_no')
        self.__title = kwargs.get('title')
        self.__first_name = kwargs.get('first_name')
        self.__middle_name = kwargs.get('middle_name')
        self.__last_name = kwargs.get('last_name')
        # jr, third
        self.__suffix = kwargs.get('suffix')
        self.__title_line = kwargs.get('title_line')
        self.__extra_addr_line = kwargs.get('extra_addr_line')
        self.__street_line = kwargs.get('street_line')
        # apt num
        self.__number = kwargs.get('number')
        self.__zip_code = kwargs.get('zip_code')
        # check or credit whatever
        self.__code_line = kwargs.get('code_line')
        self.__comm1 = kwargs.get('comm1')
        self.__mail_code = kwargs.get('mail_code')

    @property
    def pageNo(self):
        return self.__page_no

    @pageNo.setter
    def pageNo(self, v: str):
        self.__page_no = v

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, v: str):
        self.__title = v

    @property
    def firstName(self):
        return self.__first_name

    @firstName.setter
    def firstName(self, v: str):
        self.__first_name = v

    @property
    def middleName(self):
        return self.__middle_name

    @middleName.setter
    def middleName(self, v: str):
        self.__middle_name = v

    @property
    def lastName(self):
        return self.__last_name

    @lastName.setter
    def lastName(self, v: str):
        self.__last_name = v

    @property
    def suffix(self):
        return self.__suffix

    @suffix.setter
    def suffix(self, v: str):
        self.__suffix = v

    @property
    def titleLine(self):
        return self.__title_line

    @titleLine.setter
    def titleLine(self, v: str):
        self.__title_line = v

    @property
    def extraAddr(self):
        return self.__extra_addr_line

    @extraAddr.setter
    def extraAddr(self, v: str):
        self.__extra_addr_line = v

    @property
    def streetLine(self):
        return self.__street_line

    @streetLine.setter
    def streetLine(self, v: str):
        self.__street_line = v

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, v: str):
        self.__number = v

    @property
    def zipCode(self):
        return self.__zip_code

    @zipCode.setter
    def zipCode(self, v: str):
        self.__zip_code = v

    @property
    def codeLine(self):
        return self.__code_line

    @codeLine.setter
    def codeLine(self, v: str):
        self.__code_line = v

    @property
    def comm1(self):
        return self.__comm1

    @comm1.setter
    def comm1(self, v: str):
        self.__comm1 = v

    @property
    def mailCode(self):
        return self.__mail_code

    @mailCode.setter
    def mailCode(self, v: str):
        self.__mail_code = v

    @classmethod
    def of(cls, v: Dict[str, str] | None):
        if v is None:
            return None

        return cls(**v)
