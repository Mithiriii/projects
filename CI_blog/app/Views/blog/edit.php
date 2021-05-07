<section>
<div class="container">
  <h1>Edit post</h1>
  <?php if ($_POST): ?>
    <?= \Config\Services::validation()->listErrors(); ?>
  <?php endif; ?>
  <form class="" action="/blog/update/<?= $post['slug'] ?>/<?= $post['id'] ?>" method="post">
    <div class="form-group">
      <label for="title"><strong>Title:</strong></label>
      <input type="text" class="form-control" name="title" id="title" value="<?= $post['title'] ?>">
    </div>
    <div class="form-group">
      <label for="body"><strong>Body:</strong></label>
      <textarea class="form-control" name="body" id="body"><?= $post['body'] ?></textarea>
    </div>
    <div class="form-group">
      <button type="submit" class="btn brn-primary">Edit</button>
    </div>
  </form>
</div>

</section>
