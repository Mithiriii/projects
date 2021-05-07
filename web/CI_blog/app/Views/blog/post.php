<section>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm8- offset-sm-2 col-md-6 offset-md-3 mt-5 pt-3 pb-3 bg-white from-wrapper">
  <article class="blog-post">
    <h1><?= $post['title'] ?></h1>
    <div class="details">
      Posted on: <?= date('M d Y', strtotime($post['created_at'])) ?> by <?= $post['author'] ?>
    </div>
    <?= $post['body'] ?>
    <?php if ($post['author_id']==(session() ->get('id'))): ?>
    <p><div class="btn-group mr-2" role="group" aria-label="First group">
      <form class="" action="/blog/delete/<?= $post['id'] ?>" method="post">
      <button type="submit" class="btn brn-primary">Delete</button></form></div>
      <div class="btn-group mr-2" role="group" aria-label="Secondary group">
      <form class="" action="/blog/edit/<?= $post['slug'] ?>" method="post">
      <button type="submit" class="btn brn-primary">Edit</button></form></div></p>
      <?php endif; ?>
  </article>
  </div></div></div>
</section>
