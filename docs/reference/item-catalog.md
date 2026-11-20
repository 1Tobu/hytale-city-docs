# Hytale-Itemkatalog

Suche Vanilla-Items nach ihrem englischen Spielnamen oder ihrer exakten Item-ID. Der Katalog enthält auch interne Einträge wie Vorlagen und Debug-Items.

<div id="item-catalog">
  <label for="item-filter">Name oder Item-ID</label>
  <input id="item-filter" type="search" placeholder="z. B. Iron Ore oder Ore_Iron">
  <p id="item-results" role="status">Itemkatalog wird geladen …</p>
  <ul id="item-grid" class="item-grid"></ul>
  <div class="item-pagination">
    <button type="button" id="item-previous" disabled>Zurück</button>
    <span id="item-page"></span>
    <button type="button" id="item-next" disabled>Weiter</button>
  </div>
</div>
<noscript>Für die Suche und Bildanzeige muss JavaScript aktiviert sein.</noscript>
