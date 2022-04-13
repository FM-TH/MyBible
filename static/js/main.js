window.onload = async function () {
    // 検索する
    var search = async () => {
        // 入力された値でを本を検索
        var items = await searchBooks($q.value);

        // html に変換して表示用 DOM に代入
        var texts = items.map(item => {
            return `
        <a class='f border bg-white mb8' href='${item.link}', target='_blank'>
          <img class='w100 object-fit-contain bg-gray' src='${item.image}' />
          <div class='p16'>
            <h3 class='mb8'>${item.title}</h3>
            <p class='line-clamp-2'>${item.description}</p>
          </div>
        </div>`;
        });
        $results.innerHTML = texts.join('');
    };
