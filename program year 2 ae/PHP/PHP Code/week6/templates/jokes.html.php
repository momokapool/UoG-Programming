<?php 
foreach($jokes as $joke): ?>
        <blockquote>

        <?=htmlspecialchars($joke['joketext'], ENT_QUOTES,'UTF-8')?>
        <br>
        <?=htmlspecialchars($joke['name'], ENT_QUOTES, 'UTF-8') ?>
        <a href="editjoke.php">Edit</a>  

        <form action="deletejoke.php" method="post">
                <input type="hidden" name="id" value="<?=$joke['id']?>">
                <input type="submit" value="Delete">
        </form>
        </blockquote>
        <?php endforeach;?>

        