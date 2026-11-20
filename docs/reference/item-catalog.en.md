# Hytale item catalog

Find vanilla items by their in-game name or exact item ID. The catalog also includes internal definitions such as templates and debug items.

<div id="item-catalog">
  <label for="item-filter">Name or item ID</label>
  <input id="item-filter" type="search" placeholder="e.g. Iron Ore or Ore_Iron">
  <p id="item-results" role="status">Loading the item catalog …</p>
  <ul id="item-grid" class="item-grid"></ul>
  <div class="item-pagination">
    <button type="button" id="item-previous" disabled>Previous</button>
    <span id="item-page"></span>
    <button type="button" id="item-next" disabled>Next</button>
  </div>
</div>
<noscript>Enable JavaScript to search for items and display their icons.</noscript>
