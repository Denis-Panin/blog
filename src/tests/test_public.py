from blog.models import ContactUs
from django.urls import reverse


def test_home_page(client):
    response = client.get(reverse('home_page'))
    assert response.status_code == 200


def test_posts_list_csv(client):
    response = client.get(reverse('posts_list_csv'))
    assert response.status_code == 200


def test_contacts_us_show(client):
    response = client.get(reverse('contact-us-create'))
    assert response.status_code == 200


def test_posts_list(client):
    response = client.get(reverse('posts_list'))
    assert response.status_code == 200


def test_authors_all(client):
    response = client.get(reverse('authors_all'))
    assert response.status_code == 200


def test_categories_all(client):
    response = client.get(reverse('categories_all'))
    assert response.status_code == 200


def test_books_all(client):
    response = client.get(reverse('books_all'))
    assert response.status_code == 200


def test_subscribers(client):
    response = client.get(reverse('subscribers'))
    assert response.status_code == 200


def test_contacts_post_empty_form(client):
    response = client.post(reverse('contact-us-create'))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Обязательное поле.'],
        'subject': ['Обязательное поле.'],
        'message': ['Обязательное поле.']
    }


def test_contact_us_wrong_email(client):
    response = client.post(reverse('contact-us-create'), data={
        'email': 'not-valid-email'
    })
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Введите правильный адрес электронной почты.'],
        'subject': ['Обязательное поле.'],
        'message': ['Обязательное поле.']
    }


def test_contact_us_correct_form_count(client):
    count_before = ContactUs.objects.count()
    response = client.post(reverse('contact-us-create'), data={
        'email': 'test@mail.com',
        'subject': 'subj',
        'message': 'msg'
    })
    assert response.status_code == 302
    assert ContactUs.objects.count() == count_before + 1

    response = client.post(reverse('contact-us-create'), data={
        'email': 'test@mail.com',
        'subject': 'subj',
        'message': 'msg'
    })
    assert response.status_code == 302
    assert ContactUs.objects.count() == count_before + 2


def test_user(usr_fixt):
    print(usr_fixt)


def test_post(post_fixt):
    print(post_fixt)


def test_category(category_fixt):
    print(category_fixt)


def test_contactus(contactus_fixt):
    print(contactus_fixt)
