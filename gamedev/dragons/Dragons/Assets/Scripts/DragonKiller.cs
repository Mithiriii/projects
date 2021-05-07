using UnityEngine;
using UnityEngine.SceneManagement;

public class DragonKiller : MonoBehaviour
{
    // Update is called once per frame
    void Update()
    {
        if (transform.position.y > 6 || transform.position.y <-6)
            SceneManager.LoadScene(0);
    }

    public void OnCollisionEnter2D(Collision2D collision)
    {
        var enemy = collision.collider.GetComponent<Enemy>();
        if (Life.lifeCount == 1)
            SceneManager.LoadScene(0);
        else
        {
            Life.lifeCount--;            
            enemy?.Die();
        }       
    }
}
