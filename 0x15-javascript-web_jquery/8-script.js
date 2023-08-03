$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  var movies = data.results;
  var movieList = $('#list_movies');
  movies.forEach(function(movie) {
    var title = movie.title;
    var listItem = $('<li></li>').text(title);
    movieList.append(listItem);
  });
});