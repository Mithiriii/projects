using UnityEngine;

public class Enemy : MonoBehaviour
{
    public void Die()
    {
        GetComponent<SpriteRenderer>().enabled = false;
        GetComponent<Collider2D>().enabled = false;
        Score.scoreCount += 1; 
        if(Score.scoreCount % 10 == 0)
        {
            Life.lifeCount++;
        }
    }

    public void Respawn()
    {
        GetComponent<SpriteRenderer>().enabled = true;
        GetComponent<Collider2D>().enabled = true;
    }
}
