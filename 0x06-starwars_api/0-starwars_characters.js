#!/usr/bin/node
// script to get the name of starwars character
const request = require('request');

const filmId = process.argv[2];
// console.log(filmId)
const urlById = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
// console.log(urlById)
request(urlById, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  // console.error('error:', error); // Print the error if one occurred
  // console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  // console.log('body:', body); // Print the HTML for the Google homepage.

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  // console.log(characters)
  function fetchCharacter (index) {
    if (index >= characters.length) {
      return;
    }
    const characterUrl = characters[index];
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharacter(index + 1);
    });
  }
  fetchCharacter(0);
});
