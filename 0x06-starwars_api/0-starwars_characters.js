#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2]
//console.log(filmId)
const urlById = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
//console.log(urlById)
request(urlById, function (error, response, body) {
  //console.error('error:', error); // Print the error if one occurred
  //console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  //console.log('body:', body); // Print the HTML for the Google homepage.

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  characters.forEach(characterUrl => {
    request(characterUrl, function (error, response, body) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
    })
  });
});
