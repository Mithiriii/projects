<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>CI Projekt</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="/assets/css/style.css">
    </head>
  <body>
    <?php
      $uri = service('uri');
     ?>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
<div class="container">
      <a class="navbar-brand" href="/">CI Blog</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link <?= ($uri->getSegment(1) == 'about' ? 'active' : null) ?>" href="/about">About us</a>
          </li>
        </ul>
        <?php if (session()->get('isLoggedIn')): ?>
          <ul class="navbar-nav">
            <li><a href="/blog/create" class="btn btn-outline-success">Create Post</a></li>
          </ul>
          <ul class="navbar-nav">

            <li class="nav-item <?= ($uri->getSegment(2) == 'profile' ? 'active' : null) ?>"><a href="/user/profile" class="nav-link">Profile</a></li>
          </ul>
          <ul class="navbar-nav my-2 my-lg-0">
            <li class="nav-item <?= ($uri->getSegment(2) == 'logout' ? 'active' : null) ?>"><a href="/user/logout" class="nav-link">Logout</a></li>
          </ul>
        <?php else: ?>

        <ul class="navbar-nav">
          <li class="nav-item <?= ($uri->getSegment(2) == 'login' ? 'active' : null) ?>"><a href="/user/login" class="nav-link">Login</a></li>
          <li class="nav-item <?= ($uri->getSegment(2) == 'register' ? 'active' : null) ?>"><a href="/user/register" class="nav-link">Register</a></li>
        </ul>



      </div>
      <?php endif; ?>
    </div>
    </nav>
