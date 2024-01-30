#!/usr/bin/node
const request = require('request');

function getReq (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(body);
    });
  });
}

async function printCharacter (url) {
  try {
    const body = await getReq(url);
    console.log(JSON.parse(body).name);
  } catch (err) { console.error(err); }
}

async function main () {
  const Id = process.argv[2];
  const url2 = `https://swapi-api.alx-tools.com/api/films/${Id}/`;

  try {
    const body = await getReq(url2);
    const charList = JSON.parse(body).characters;
    for (const Url of charList) {
      await printCharacter(Url);
    }
  } catch (err) { console.error(err); }
}

main();
