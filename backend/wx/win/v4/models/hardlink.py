from sqlalchemy import Column, String, Integer, LargeBinary, Float

from wx.win.v4.db.windows_v4_db import Base


class DBInfoModel(Base):
    __tablename__ = 'db_info'

    Key = Column(String, primary_key=True)
    ValueInt64 = Column(Integer)
    ValueDouble = Column(Float)
    ValueStdStr = Column(String)
    ValueBlob = Column(LargeBinary)


class Dir2IdModel(Base):
    __tablename__ = "dir2id"

    username = Column(String, primary_key=True)


class VideoHardlinkInfoModelV3(Base):
    __tablename__ = 'video_hardlink_info_v3'

    md5_hash = Column(Integer, primary_key=True)
    md5 = Column(String)
    type = Column(Integer)
    file_name = Column(String)
    file_size = Column(Integer)
    modify_time = Column(Integer)
    dir1 = Column(Integer)
    dir2 = Column(Integer)
    _rowid_ = Column(Integer)
    extra_buffer = Column(LargeBinary)


class ImageHardlinkInfoModelV3(Base):
    __tablename__ = 'image_hardlink_info_v3'

    md5_hash = Column(Integer, primary_key=True)
    md5 = Column(String)
    type = Column(Integer)
    file_name = Column(String)
    file_size = Column(Integer)
    modify_time = Column(Integer)
    dir1 = Column(Integer)
    dir2 = Column(Integer)
    _rowid_ = Column(Integer)
    extra_buffer = Column(LargeBinary)



class VideoHardlinkInfoModelV4(Base):
    __tablename__ = 'video_hardlink_info_v4'

    md5_hash = Column(Integer, primary_key=True)
    md5 = Column(String)
    type = Column(Integer)
    file_name = Column(String)
    file_size = Column(Integer)
    modify_time = Column(Integer)
    dir1 = Column(Integer)
    dir2 = Column(Integer)
    _rowid_ = Column(Integer)
    extra_buffer = Column(LargeBinary)


class ImageHardlinkInfoModelV4(Base):
    __tablename__ = 'image_hardlink_info_v4'

    md5_hash = Column(Integer, primary_key=True)
    md5 = Column(String)
    type = Column(Integer)
    file_name = Column(String)
    file_size = Column(Integer)
    modify_time = Column(Integer)
    dir1 = Column(Integer)
    dir2 = Column(Integer)
    _rowid_ = Column(Integer)
    extra_buffer = Column(LargeBinary)