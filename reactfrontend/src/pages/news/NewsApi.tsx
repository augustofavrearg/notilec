export function searchNews(){
    if (!localStorage['news']){
        localStorage['news'] = '[]';
    }
    let news = localStorage['news'];
    news = JSON.parse(news);
    return news;
}

export function saveNews(newItem: any) {
    let news = searchNews(); // Asumiendo que searchNews() está definida en otro lugar
    news.push(newItem);
    localStorage['news'] = JSON.stringify(news);
}
