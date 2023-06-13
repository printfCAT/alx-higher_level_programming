#!/usr/bin/node
exports.esrever = function (list) {
  const store = [];
  for (let i = list.length - 1; i >= 0; i--) {
    store.push(list[i]);
  }
  return store;
};
