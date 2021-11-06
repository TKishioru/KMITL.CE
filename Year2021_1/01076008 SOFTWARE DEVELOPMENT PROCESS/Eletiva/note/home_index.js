const searchBtn = document.getElementById('search-button');
const search = document.getElementById('search');
const searchtext = document.getElementById('searchtext');
const searchCL = document.getElementById('searchclass')

searchCL.addEventListener('click', () => {
    search.style.display = 'block';
    search.style.width = '30%';
    search.style.paddingRight = '50px';
    search.style.right = '220px';
    searchBtn.style.color = '#FAB23D';
    searchBtn.style.position = 'absolute';
    searchBtn.style.top = '17px';
    searchBtn.style.cursor = 'pointer';
    searchCL.style.pointerEvents = 'none';
    searchtext.style.display = 'none';
})