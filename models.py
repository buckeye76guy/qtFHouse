import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date, DateTime

Base = declarative_base()

_active_clients_table_name = 'active_clients'
_deleted_clients_table_name = 'deleted_clients'
_service_logs_table_name = 'service_logs'


def _capitalize(word: str):
    """

    :param word: A word or text to capitalize
    :return: a capitalized version of the string
    """
    if not isinstance(word, str):
        return word
    # one word
    word = word.strip()

    if len(word.split(' ')) == 1:
        # if there is no hyphen
        if len(word.split('-')) == 1:
            return word.capitalize()
        # if there is a hyphen
        else:
            return '_'.join([el.capitalize() for el in word.split('-')])
    # more than 1
    else:
        return ' '.join([_capitalize(wd) for wd in word.split(' ')])


def _user_id_maker(last_name: str, first_name: str, dob: dt.date):
    """

    :param last_name: a last name
    :param first_name: a first name
    :param dob: the date of birth
    :return: a custom concatenation of all 3
    """
    return "%s|%s|%s" % (last_name.lower(), first_name.lower(), dob.strftime("%m_%d_%Y"))


# TODO: add more columns and add them to the init function
class Clients(Base):
    __tablename__ = _active_clients_table_name

    first_name = Column(String(100), primary_key=True)
    last_name = Column(String(100), primary_key=True)
    date_of_birth = Column(Date, primary_key=True)
    user_id = Column(String(100))
    race = Column(String(100))
    gender = Column(String(100))
    join_date = Column(Date)
    last_updt_dt = Column(Date)

    def __init__(self, first_name: str, last_name: str, date_of_birth, race, gender, join_date,
                 last_updt_dt=dt.date.today()):
        self.first_name = _capitalize(first_name)
        self.last_name = _capitalize(last_name)
        self.date_of_birth = date_of_birth
        self.user_id = _user_id_maker(last_name.strip(), first_name.strip(), date_of_birth)
        self.race = race
        self.gender = gender
        self.join_date = join_date
        self.last_updt_dt = last_updt_dt


class Archived(Base):
    __tablename__ = _deleted_clients_table_name

    first_name = Column(String(100), primary_key=True)
    last_name = Column(String(100), primary_key=True)
    date_of_birth = Column(Date, primary_key=True)
    user_id = Column(String(100))
    race = Column(String(100))
    gender = Column(String(100))
    join_date = Column(Date)
    archive_date = Column(Date)
    last_updt_dt = Column(Date)

    def __init__(self, first_name: str, last_name: str, date_of_birth, race, gender, join_date, archive_date,
                 last_updt_dt=dt.date.today()):
        self.first_name = _capitalize(first_name)
        self.last_name = _capitalize(last_name)
        self.date_of_birth = date_of_birth
        self.user_id = _user_id_maker(last_name.strip(), first_name.strip(), date_of_birth)
        self.race = race
        self.gender = gender
        self.join_date = join_date
        self.archive_date = archive_date
        self.last_updt_dt = last_updt_dt


class ServiceLogs(Base):
    __tablename__ = _service_logs_table_name

    first_name = Column(String(100), primary_key=True)
    last_name = Column(String(100), primary_key=True)
    date_of_birth = Column(Date, primary_key=True)
    user_id = Column(String(100))
    service_date = Column(DateTime)
