from celery import shared_task


@shared_task()
def increment_ranks(a, b):
    sum = a + b
    print(sum)
