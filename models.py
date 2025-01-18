from sqlalchemy import Table, Column, Integer, String, ForeignKey, UniqueConstraint
from database import metadata

users = Table(
    'users',
    metadata,
    Column('users_id', Integer, primary_key=True),
    Column('username', String(45)),
    Column('email', String(45)),
    Column('password', String(45)),
    Column('blog_blog_id', Integer, unique=True),
    Column('contact_id_name1', String(45), unique=True),
    UniqueConstraint('blog_blog_id', name='unique_blog_blog_id'),
    UniqueConstraint('contact_id_name1', name='unique_contact_id')
)

blog = Table(
    'blog',
    metadata,
    Column('blog_id', Integer, primary_key=True),
    Column('title', String(45)),
    Column('content', String(45)),
    Column('users_blog_blog_id', Integer, ForeignKey('users.blog_blog_id')),
    UniqueConstraint('blog_id', name='unique_blog_id')
)

pets = Table(
    'pets',
    metadata,
    Column('pet_id', Integer, primary_key=True),
    Column('pet_name', String(45)),
    Column('pet_type', String(45)),
    Column('pet_age', String(45)),
    Column('blog_blog_id', Integer, unique=True),
    UniqueConstraint('blog_blog_id', name='pets_blog_blog_id_key')
)


sterilization = Table(
    'sterilization',
    metadata,
    Column('sterilization_id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('pet_id', Integer),
    Column('animal_type', String(45)),
    Column('animal_age', String(45)),
    Column('animal_gender', String(45)),
    Column('animal_weight', String(45)),
    Column('vet_name', String(45)),
    Column('vet_contact', String(45)),
    Column('vet_address', String(45)),
    Column('owner_name', String(45)),
    Column('owner_sign', String(45)),
    Column('pets_pet_id', Integer, ForeignKey('pets.pet_id')),
    Column('pets_blog_blog_id', Integer, ForeignKey('pets.blog_blog_id')),
    Column('users_users_id', Integer, ForeignKey('users.users_id')),
    Column('users_blog_blog_id', Integer, ForeignKey('users.blog_blog_id')),
    Column('users_contact_id_name1', String(45), ForeignKey('users.contact_id_name1'))
)

contact = Table(
    'contact',
    metadata,
    Column('id_name1', String(45), primary_key=True),
    Column('name', String(45)),
    Column('email', String(45)),
    Column('phone', String(45)),
    Column('message', String(45)),
    Column('users_contact_id_name1', String(45), ForeignKey('users.contact_id_name1')),
    UniqueConstraint('id_name1', name='unique_id_name1')
)
