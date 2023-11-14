#!/usr/bin/node

const { dict } = require('./101-data');

function invertDictionary (Odict) {
  const Idict = {};

  for (const id in Odict) {
    const occu = Odict[id];

    if (occu in Idict) {
      Idict[occu].push(id.toString());
    } else {
      Idict[occu] = [id.toString()];
    }
  }

  return Idict;
}

const Idict = invertDictionary(dict);
console.log(Idict);
