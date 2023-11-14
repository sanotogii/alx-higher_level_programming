#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || Number.isInteger(w) || Number.isInteger(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
