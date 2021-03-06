from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, youtube_id) -> None:
        self.slug = slug
        self.titulo = titulo

    def get_absolut_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('01', 'Café com Analytics: 01', 'McQ-DttWgwU'),
    Video('02', 'Café com Analytics: 02', 'vD8C541oT4k')
    ]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
